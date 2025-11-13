import React from 'react';
import { ScrollView, Dimensions, StyleSheet } from 'react-native';
import RenderHtml from 'react-native-render-html';

export default function ArticleScreen({ route }) {
  const { article } = route.params;
  const contentWidth = Dimensions.get('window').width;

  // Use article.content as HTML string from your backend
  return (
    <ScrollView style={styles.container}>
      <RenderHtml
        contentWidth={contentWidth}
        source={{ html: article.content }}
        tagsStyles={{
          h1: { fontSize: 22, fontWeight: 'bold', marginVertical: 10 },
          h2: { fontSize: 18, fontWeight: '600', marginVertical: 8 },
          p: { fontSize: 16, lineHeight: 24 },
          img: { borderRadius: 10, marginVertical: 10, width: '100%' },
        }}
      />
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 10,
    backgroundColor: '#f0f2f5',
  },
});
